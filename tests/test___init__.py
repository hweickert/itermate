import itermate



assert [1, 2, 3, 6] == list( itermate.imapchain(lambda n: (n, n*2), [1, 3]) )
assert [1, 2] ==       list( itermate.unique([1, 2, 1, 2]) )
