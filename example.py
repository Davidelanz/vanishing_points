# https://stackoverflow.com/questions/4931376/generating-matplotlib-graphs-without-a-running-x-server
import matplotlib
matplotlib.use('Agg')

if __name__ == "__main__":
    from vp_detector.example import run_examples

    data_folder = {"name": "test_alina",
                   "source_folder": "test_alina/images",
                   "destination_folder": "test_alina/results"}

    # Run
    run_examples(gpu_id=None, show=False, data_folder=data_folder)
    # Then show
    run_examples(gpu_id=None, show=True, data_folder=data_folder)
