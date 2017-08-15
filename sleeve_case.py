# -*- coding: utf-8 -*-

GIRDER = "GIRDER_TYPE"  # 大梁タイプ
BEAM = "BEAM_TYPE"      # 小梁タイプ
CANTILEVER = "CANTILEVER_TYPE"  # 片持ち梁タイプ



class Position:
    def __init__(self, sou = "2階", frame="4通り", jiku_r="4", jiku_l="5"):
        self.sou = sou
        self.frame = frame
        self.jiku_r = jiku_r
        self.jiku_l = jiku_l


class SleeveCheckCase:
    def __init__(self, name="Untitled", span=6000., _type=GIRDER):
        self.name = name
        self.span = span

        pass
