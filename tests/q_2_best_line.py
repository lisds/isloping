test = {
  'name': 'Question 2_best_line',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'best_inter' and 'best_slope'
          >>> 'best_inter' in vars()
          True
          >>> 'best_slope' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'best_inter' and / or
          >>> # 'best_slope'
          >>> # from their initial state (of ...)
          >>> best_inter is not ...
          True
          >>> best_slope is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose([best_inter, best_slope], [12.769185, -0.77302])
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
