import datetime


def unique_id_generator(id):
    app = "TICKET"
    date = datetime.datetime.now().strftime("%Y%m%d")
    id_format = '{:06}'.format(id)

    unique_id = app + date + '-' + id_format

    return unique_id
