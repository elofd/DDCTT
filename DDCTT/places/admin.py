"""
Admin for places app
"""
from django.contrib.gis import admin
from django.http import HttpResponse
from leaflet.admin import LeafletGeoAdmin
import xlsxwriter

from .models import Place, WeatherInPlace


admin.site.register(Place, LeafletGeoAdmin)


@admin.register(WeatherInPlace)
class WeatherInPlaceAdmin(admin.ModelAdmin):
    """
    class WeatherInPlaceAdmin for WeatherInPlace model
    """
    list_display = 'place', 'temp', 'humidity', 'pressure', 'wind_deg', 'wind_speed', 'date_of_reading'
    list_filter = 'place', 'date_of_reading'
    readonly_fields = 'place', 'temp', 'humidity', 'pressure', 'wind_deg', 'wind_speed', 'date_of_reading'

    actions = ['export_to_xlsx', ]

    def export_to_xlsx(self, request, queryset):
        """
        Action export of selected objects to xls file
        """
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="weather_data.xlsx"'

        workbook = xlsxwriter.Workbook(response, {'in_memory': True})
        worksheet = workbook.add_worksheet()

        headers = ['Place', 'Date of Reading', 'Temperature', 'Humidity', 'Wind Speed']
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header)

        row_num = 1
        for obj in queryset:
            row = [obj.place, obj.date_of_reading, obj.temp, obj.humidity, obj.wind_speed]
            for col_num, cell_value in enumerate(row):
                worksheet.write(row_num, col_num, str(cell_value))
            row_num += 1

        workbook.close()
        return response

    export_to_xlsx.short_description = 'Export to XLSX'

    def has_add_permission(self, request):
        """
        delete add permissions from admin and add button
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        delete delete permissions from admin and delete button
        """
        return False
