from teman.models import daftar_temans

# function
def run_view():
    print('==== daftar teman ====')
    for teman in daftar_temans:
        print(teman)