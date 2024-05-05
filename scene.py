from manim import *

class Scene1(Scene):
    def intro(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        autolayouts = ["spring", "circular", "kamada_kawai",
                       "planar", "random", "shell",
                       "spectral", "spiral"]
        graphs = [Graph(vertices, edges, layout=lt).scale(0.5)
                  for lt in autolayouts]
        r1 = VGroup(*graphs[:3]).arrange().shift(UP*2.5)
        r2 = VGroup(*graphs[3:6]).arrange()
        r3 = VGroup(*graphs[6:]).arrange().shift(DOWN*2.5)
        self.play(Create(r1), Create(r2), Create(r3), run_time=2)
        self.wait()
        self.play(FadeOut(r1), FadeOut(r2), FadeOut(r3), run_time=1)
        edges = []
        partitions = []
        c = 0
        layers = [2, 3, 3, 2]  # the number of neurons in each layer

        for i in layers:
            partitions.append(list(range(c + 1, c + i + 1)))
            c += i
        for i, v in enumerate(layers[1:]):
                last = sum(layers[:i+1])
                for j in range(v):
                    for k in range(last - layers[i], last):
                        edges.append((k + 1, j + last + 1))

        vertices = np.arange(1, sum(layers) + 1)

        graph = Graph(
            vertices,
            edges,
            layout='partite',
            partitions=partitions,
            layout_scale=3,
            vertex_config={'radius': 0.20},
        )
        self.play(Create(graph), run_time=2)
        self.wait()
        self.play(FadeOut(graph), run_time=1)
        self.wait()
    
    def metro(self):
        #metro station
        stations = {
            "A": [0, -3, 0],
            "B": [0, -2, 0],
            "C": [0, -1, 0],
            "D": [1, 0, 0],
           #"E": [1, -2, 0],
           #"F": [0,-1, 0],
           #"G": [2, -1, 0],
        }
        edges = [
            ("A", "B", BLUE),
            ("B", "C", BLUE),
            ("C", "D", BLUE),

        ]

        # Create station dots
        for station, pos in stations.items():
            dot = Dot(point=pos, color=WHITE)
            self.play(Create(dot), run_time=0.4)

        # Draw lines
        for start, end, color in edges:
            line = Line(start=stations[start], end=stations[end], color=color, stroke_width=8)
            self.play(Create(line), run_time=0.4)

        self.wait(1)
        
    

    def construct(self):
        self.metro()
