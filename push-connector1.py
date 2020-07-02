import cadquery as cq # type: ignore

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

thing = r1.revolve(360, (0, 0, 0), (1, 0, 0))
