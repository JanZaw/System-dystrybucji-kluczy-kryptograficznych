import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Dane dla wykresu Gantta
tasks = ['Modlenie się by działało','Sprawdzanie czy działa', 'Pisanie kodu dystrubycji', 'Pisanie kodu dla zarządzania', 'Pisanie systemu bezpieczeństwa']
start_dates = ['2024-04-22','2024-04-23', '2024-04-22', '2024-04-28', '2024-05-09']
end_dates = ['2024-05-19','2024-05-19', '2024-04-29', '2024-05-08', '2024-05-19']

# Konwersja dat na format matplotlib
start_dates = [mdates.datestr2num(date) for date in start_dates]
end_dates = [mdates.datestr2num(date) for date in end_dates]

# Utworzenie subplotu
fig, ax = plt.subplots()

# Ustawienie osi X jako daty
ax.xaxis_date()

# Ustawienie tytułu i etykiet osi
ax.set_title('System dystrybucji kluczy kryptograficznych')
ax.set_xlabel('Czas który będzie psędzony na robieniu')
ax.set_ylabel('Zadania')

# Dodanie słupków dla każdego zadania
for i, task in enumerate(tasks):
    ax.barh(task, end_dates[i] - start_dates[i], left=start_dates[i])

# Ustawienie formatu dat na osi X
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Pokaż wykres
plt.tight_layout()
plt.savefig('wykres_gantta.png')
plt.show()