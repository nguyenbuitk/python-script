import argparse

# Define a list of clusters for the example
clusters = [
    {'cluster': 'cluster1', 'url': 'http://cluster1.example.com'},
    {'cluster': 'cluster2', 'url': 'http://cluster2.example.com'},
    {'cluster': 'cluster3', 'url': 'http://cluster3.example.com'}
]

def main():
    # Create the parser
    parser = argparse.ArgumentParser(
            description='Process some clusters.',
            epilog='Example usage: python3 cluster_script.py -c prod-us')

    # Add the cluster argument
    parser.add_argument(
        '-c', '--cluster',
        dest='cluster',
        action='store',
        metavar='cluster',
        choices=[cluster['cluster'] for cluster in clusters],
        help='The cluster name',
        required=True
    )

    # Add another argument for verbosity (example of optional argument)
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Increase output verbosity'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Use the parsed arguments
    print(f'Selected cluster: {args.cluster}')
    if args.verbose:
        print('Verbose mode enabled.')

    # Find the URL of the selected cluster
    selected_cluster = next(cluster for cluster in clusters if cluster['cluster'] == args.cluster)
    url = selected_cluster['url']

    print(f'URL of the selected cluster: {url}')

if __name__ == '__main__':
    main()
