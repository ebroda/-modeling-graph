from openpyxl import load_workbook

from hybit_graph.classes import Node, Edge


def load_data(filename):
    wb = load_workbook(filename=filename)
    sheet = wb.active

    nodes = {}
    edges_weight = {}
    edges = []

    for row in sheet.iter_rows(min_row=5, max_col=6):
        source_id = None
        sink_id = None

        # source
        if row[2].value is not None and len(str(row[2].value)) > 0:
            # valid node
            source_id = str(row[2].value).strip()
            if source_id not in nodes:
                nodes[source_id] = Node(source_id)
        else:
            print("Missing source id in %s, line ignored" % row[2].coordinate)
            continue

        # sink
        if source_id and row[5].value is not None and len(str(row[5].value)) > 0:

            targets = str(row[5].value).split(";")

            for target in targets:
                # valid node
                sink_id = target.strip()
                if sink_id not in nodes:
                    nodes[sink_id] = Node(sink_id)

                if source_id and sink_id:
                    # add edge
                    edge = Edge(row[0].value, row[1].value, row[3].value, row[4].value)
                    edge.node_in = nodes[source_id]
                    edge.node_out = nodes[sink_id]

                    nodes[source_id].edges_out.append(edge)
                    nodes[sink_id].edges_in.append(edge)
                    edges.append(edge)
                    if source_id not in edges_weight:
                        edges_weight[source_id] = {}

                    if sink_id not in edges_weight[source_id]:
                        edges_weight[source_id][sink_id] = 0

                    edges_weight[source_id][sink_id] += 1
        else:
            print("Missing sink id in %s, line ignored" % row[5].coordinate)

    return nodes, edges, edges_weight
