from menpo.shape import TriMesh

def utils_mesh():
    trilist = np.array([[0, 1, 2],
                    [0, 2, 3]])
    points = np.array([[0, 0],
                       [1, 0],
                       [1, 1],
                       [0, 1]])
    return TriMesh(points, trilist=trilist)


gt_edge_indices = np.array([[0, 1],
                            [0, 2],
                            [1, 2],
                            [2, 3],
                            [2, 0],
                            [3, 0]])

gt_edges = np.array([[ 1,  0],
                     [ 1,  1],
                     [ 0,  1],
                     [-1,  0],
                     [ 1,  1],
                     [ 0,  1]])

gt_edge_lengths = np.array([ 1.     ,  1.41421356,  1.        ,  1.        ,  1.41421356,  1.        ])

gt_unique_edge_lengths = np.array([ 1.        ,  1.41421356,  1.        ,  1.        ,  1.        ])

gt_face_areas = np.array([ 0.5,  0.5])


def test_edge_indices():
    assert np.all(utils_mesh().edge_indices() == gt_edge_indices)


def test_edges():
    assert np.all(utils_mesh().edges() == gt_edges)


def test_edge_lengths():
    assert np.allclose(utils_mesh().edge_lengths(), gt_edge_lengths)


def test_unique_edge_lengths():
    assert np.allclose(utils_mesh().unique_edge_lengths(), gt_unique_edge_lengths)


def test_face_areas():
    assert np.allclose(utils_mesh().face_areas(), gt_face_areas)


def test_mean_face_area():
    assert utils_mesh().mean_face_area() == 0.5


def test_mean_edge_length():
    assert np.allclose(utils_mesh().mean_edge_length(), np.mean(gt_unique_edge_lengths))

def test_mean_edge_length_not_unique():
    assert np.allclose(utils_mesh().mean_edge_length(unique=False), np.mean(gt_edge_lengths))
