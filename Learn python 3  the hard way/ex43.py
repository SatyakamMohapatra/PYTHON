import ex43_map
import ex43_engine

a_map = ex43_map.Map("CentralCorridor")
print(a_map)
a_game = ex43_engine.Engine(a_map)
a_game.play
