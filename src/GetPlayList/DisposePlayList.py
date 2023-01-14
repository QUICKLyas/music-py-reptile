import config.t_file as tf


class DisposePlayList(object):
    def __init__(self) -> None:
        pass

    def parsePl(self, context):
        pls = context['playlist']

        for pl in pls:
            print(pl)
        return

    def writePltoJson(self, context):
        tf.writeJson(context, file_name="playlist")
