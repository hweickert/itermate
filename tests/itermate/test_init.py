import itermate



def test_imapchain_works():
    assert [1, 2, 3, 6] == list( itermate.imapchain(lambda n: (n, n*2), [1, 3]) )


def test_unique_works():
    assert [1, 2] ==  list( itermate.unique([1, 2, 1, 2]) )
