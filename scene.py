from manim import *

SVG_FOLDER = "svg"
FROM_SVG = lambda name: SVG_FOLDER + "/" + name + ".svg"  # I'll use an inline (which on python can be translated into lambda) that should be faster to execute unlike a normal function  - Nex

class Scene1(Scene):
    def intro(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5), (2, 8), (3, 4), (6, 1), (6, 2), (6, 3), (7, 2), (7, 4)]
        autolayouts = ["spring", "circular", "kamada_kawai", "planar", "random", "shell", "spectral", "spiral"]
        graphs = [Graph(vertices, edges, layout = lt).scale(0.5) for lt in autolayouts]
        r1 = VGroup(*graphs[:3]).arrange().shift(UP * 2.5)
        r2 = VGroup(*graphs[3:6]).arrange()
        r3 = VGroup(*graphs[6:]).arrange().shift(DOWN * 2.5)
        self.play(Create(r1), Create(r2), Create(r3), run_time = 2)
        self.wait()
        self.play(FadeOut(r1), FadeOut(r2), FadeOut(r3), run_time = 1)

    def neural_network(self):
        edges = []
        partitions = []
        c = 0
        layers = [2, 3, 3, 2]  # The number of neurons in each layer

        for i in layers:
            partitions.append(list(range(c + 1, c + i + 1)))
            c += i

        for i, v in enumerate(layers[1:]):
            last = sum(layers[:i + 1])
            for j in range(v):
                for k in range(last - layers[i], last):
                    edges.append((k + 1, j + last + 1))

        vertices = np.arange(1, sum(layers) + 1)
        graph = Graph(
            vertices,
            edges,
            layout = 'partite',
            partitions = partitions,
            layout_scale = 3,
            vertex_config = {'radius': 0.20},
        )

        self.play(Create(graph), run_time = 2)
        self.wait()
        self.play(FadeOut(graph), run_time = 1)
        self.wait()

    def metro(self):
        # Initialize groups for dots and lines
        dots = VGroup()
        lines = VGroup()

        # Metro stations setup
        stations = {
            "A": [0, -3, 0],  "B": [0, -2, 0],  "C": [0, -1, 0],
            "D": [1,  0, 0],  "E": [1, -2, 0],  "F": [0, -1, 0],
            "G": [2, -1, 0],  "H": [2,  0, 0],  "I": [2,  1, 0],
            "J": [2,  2, 0],  "K": [-3, 2, 0],  "L": [-2, 2, 0],
            "M": [-1, 2, 0],  "N": [0,  1, 0],  "O": [1,  0, 0],
            "P": [2, -1, 0],  "Q": [3,  0, 0],  "R": [4, -1, 0]
        }
        edges = [
            ("A", "B",  BLUE), ("B", "C",  BLUE), ("C", "D",  BLUE),
            ("E", "G",   RED), ("G", "H",   RED), ("H", "I",   RED),
            ("I", "J",   RED), ("K", "L", GREEN), ("L", "M", GREEN),
            ("M", "N", GREEN), ("N", "O", GREEN), ("O", "P", GREEN),
            ("P", "Q", GREEN), ("Q", "R", GREEN)
        ]

        # Create dots
        for data in stations.items():
            dot = Dot(point = data[1], color = WHITE)
            self.play(Create(dot), run_time = 0.1)
            dots.add(dot)  # Add dot to group

        # Create lines
        for start, end, color in edges:
            line = Line(start = stations[start], end = stations[end], color = color, stroke_width = 8)
            self.play(Create(line), run_time = 0.3)
            lines.add(line)  # Add line to group

        # Pause to view the scene
        self.wait()

        # Fade out all dots and lines
        self.play(FadeOut(dots), FadeOut(lines))
        self.wait()


    def bank(self):
        banks = VGroup()
        coins = VGroup()

        for pos in [LEFT, RIGHT, UP, DOWN]:
            bank = SVGMobject(FROM_SVG("bank")).scale(0.3)
            self.play(FadeIn(bank.shift(pos * 2)), run_time = 0.7)
            banks.add(bank)

        for index, pos in [[3, LEFT], [3, RIGHT], [2, LEFT], [2, DOWN]]:
            coin = SVGMobject(FROM_SVG("coin")).scale(0.2)
            self.play(FadeIn(coin.next_to(banks[index], pos)), run_time = 0.7)
            coins.add(coin)

        # Move coin to bank 2
        self.play(coins[0].animate.next_to(banks[0], LEFT), run_time = 0.7)
        self.play(coins[3].animate.next_to(banks[1], RIGHT), run_time = 0.7)
        self.wait(2)

        self.play(FadeOut(banks), FadeOut(coins))
        self.wait()

    def servers(self):
        vertices = [1, 2, 3, 4, 5, 6, 7]
        edges = [(1, 7), (2, 4), (1, 4), (4, 6), (5, 6), (6, 3), (3, 7)]
        graphics = {}

        for num in vertices:
            dot = Dot(radius = 0.3)
            server = SVGMobject(FROM_SVG("server")).scale(0.17)
            server.insert(0, dot)
            graphics[num] = server

        #SVG
        graph = Graph(vertices, edges, layout = 'circular', layout_scale = 3, vertex_mobjects = graphics)
        self.play(Create(graph), run_time = 4)
        self.wait(6)

        # The solution algorithm

    def test(self):
        # Create vertical lines one next to the other
        dots = VGroup()
        lines = VGroup()
        for i in range(1, 8):
            dot = Dot(point = DOWN * 5, color = RED).next_to(dots, RIGHT * 2)
            line = Line(start = DOWN * 3, end = DOWN, color = WHITE).next_to(lines, RIGHT * 2)
            lines.add(line)
            dots.add(dot)
        self.play(Create(lines), run_time = 4)
        self.play(Create(dots), run_time = 4)

    def construct(self):
        self.intro()
        self.neural_network()
        self.metro()
        self.bank()
        self.servers()
        #self.test()