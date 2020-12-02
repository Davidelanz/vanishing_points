# https://stackoverflow.com/questions/4931376/generating-matplotlib-graphs-without-a-running-x-server
import matplotlib
matplotlib.use('Agg')

def test_main():

    from vp_detector.example import run_examples

    data_folder = {"name" : "test",
                   "source_folder": "test/images",
                   "destination_folder": "test/results"}

    # Run
    run_examples(gpu_id=None, show=False, data_folder=data_folder)
    # Then show
    run_examples(gpu_id=None, show=True, data_folder=data_folder)
