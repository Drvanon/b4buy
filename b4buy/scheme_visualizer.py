import click
import yaml
from pprint import pprint
from yaml import Loader
from graphviz import Digraph

@click.command()
@click.argument('input_file', type=click.File())
@click.option('--verbose', '-v', is_flag=True)
def visualize_scheme(input_file, verbose):
    buildings = yaml.load(input_file, Loader=Loader)

    all_producers = {
        product: [
            building_name
            for building_name, building_data in buildings.items()
            if product in building_data['products'].keys()
        ]
        for building in buildings.values()
        for product in building['products'].keys()
    }
    all_consumers = {
        product: [
            building_name
            for building_name, building_data in buildings.items()
            if product in building_data['educts'].keys()
        ]
        for building in buildings.values()
        for product in building['educts'].keys()
    }
    edges = [
        (producer, consumer, product)
        for product, consumers in all_consumers.items()
        for producer in all_producers[product]
        for consumer in consumers
    ]
    if verbose:
        print('Consumers:')
        pprint(all_consumers)
        print('Producers:')
        pprint(all_producers)
        print('Edges:')
        pprint(edges)

    dot = Digraph()
    for building in buildings.keys():
        dot.node(building)

    for edge in edges:
        dot.edge(edge[0], edge[1], label=edge[2])

    dot.view()

if __name__ == "__main__":
    visualize_scheme()
