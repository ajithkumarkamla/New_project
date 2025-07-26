# analysis/views.py
import pandas as pd
from django.shortcuts import render
from .forms import UploadCSVForm

def upload_file(request):
    chart_data = None
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file)

            # Preprocessing
            df.drop_duplicates(inplace=True)
            df.fillna(0, inplace=True)
            df['Date'] = pd.to_datetime(df['Date'])

            india = df[df['Country'] == 'India']
            india = india.groupby('Date')[['Confirmed', 'Deaths', 'Recovered']].sum()

            chart_data = {
                'dates': india.index.strftime('%Y-%m-%d').tolist(),
                'confirmed': india['Confirmed'].tolist(),
                'deaths': india['Deaths'].tolist(),
                'recovered': india['Recovered'].tolist()
            }
    else:
        form = UploadCSVForm()
    return render(request, 'analysis/upload.html', {'form': form, 'chart_data': chart_data})
