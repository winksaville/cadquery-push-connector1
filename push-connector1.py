import cadquery as cq # type: ignore
from typing import List, Tuple

X = 0
Y = 1
Z = 2

def verticesAsList(
        wp #: cq.Workplane
) -> List[Tuple[float,float]]:
    l: List[Tuple[float, float]] = []
    for i in wp.vertices().vals():
        l.append((i.X, i.Y))
    return l

# MUST be a better way to create a cricle
p = (
    cq.Workplane("XY")
    .polygon(100, 1, forConstruction=True)
)
# Get the vertices of almost circle and append first vert to close
circle = verticesAsList(p)
circle.append((circle[0][X], circle[0][Y]))

lenOd=1
lenId=1
od=0.5
id=0.25
outline = [
      (0, 0)
    , (0, id)
    , (lenId, id)
    , (lenId, od)
    , (lenId+lenOd, id + ((od - id) / 2))
    , (lenId+lenOd, 0)
]

r1 = (
    cq.Workplane("XY")
    .polyline(outline).close()
)

thing = r1.sweep(
    cq.Workplane("YZ")
    .spline(circle)
)
