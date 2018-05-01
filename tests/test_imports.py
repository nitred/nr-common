"""Test imports for the modules that don't have tests yet."""


def test_imports(hello_world):
    """Run a test."""
    import nr_common
    from nr_common.blueprints import job_status

    from nr_common.image_utils.image_utils_cv2 import load_image as load_image_cv2
    from nr_common.image_utils.image_utils_cv2 import show_image as show_image_cv2
    from nr_common.image_utils.image_utils_meta import load_image as load_image_meta
    from nr_common.image_utils.image_utils_meta import transform_image as transform_image_meta

    from nr_common.fs_utils import makedirs

    from nr_common.configreader import read_config
    from nr_common.pickler import read_pickle, write_pickle
    from nr_common.mproc import mproc_func, mproc_async

    # Test __init__
    assert hasattr(nr_common, '__version__')

    # Test pytest fixtures
    assert(hello_world == "Hello World!")
