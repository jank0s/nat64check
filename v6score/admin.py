from django.contrib import admin
from django.utils.safestring import mark_safe

from v6score.models import Measurement, Website


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('hostname',)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('website', 'requested', 'started', 'finished', 'v6only_score', 'nat64_score')
    readonly_fields = ('requested', 'admin_images_inline',)

    fieldsets = [
        ('Test', {
            'fields': ('website', 'requested', 'started', 'finished')
        }),
        ('Results', {
            'fields': ('v6only_score', 'nat64_score')
        }),
        ('Images', {
            'fields': ('admin_images_inline',)
        }),
    ]

    def admin_images_inline(self, measurement):
        img = """<a href="{1}" target="_blank"><img style="width: 100%" alt="{0}" src="{1}"></a>"""

        return mark_safe("""
            <table style="border:0; width: 100%;">
                <tr>
                    <th style="text-align:center">IPv4-only</th>
                    <th style="text-align:center">IPv6-only</th>
                    <th style="text-align:center">NAT64</th>
                </tr>
                <tr>
                    <td style="width:33%">{v4only_image}</td>
                    <td style="width:33%">{v6only_image}</td>
                    <td style="width:33%">{nat64_image}</td>
                </tr>
            </table>
        """.format(
            v4only_image=img.format("IPv4-only", measurement.v4only_image.url) if measurement.v4only_image else '',
            v6only_image=img.format("IPv6-only", measurement.v6only_image.url) if measurement.v6only_image else '',
            nat64_image=img.format("NAT64", measurement.nat64_image.url) if measurement.nat64_image else '',
        ))

    admin_images_inline.short_description = 'Images'