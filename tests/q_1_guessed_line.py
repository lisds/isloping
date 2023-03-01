test = {
  'name': 'Question 1_guessed_line',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'rmse_guessed'
          >>> 'rmse_guessed' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'ss_guesssed'
          >>> # from its initial state (of ...)
          >>> rmse_guessed is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You appear to have the result of a "minimize", but the
          >>> # answer should be a number for the sum of squares for the
          >>> # guessed slope, rather than the best slope.
          >>> # Here a minimize results object.
          >>> hasattr(rmse_guessed, 'fun')
          False
          >>> # Here an array with more than one element.
          >>> hasattr(rmse_guessed, 'size') and rmse_guessed.size > 1
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The answer should be a number for the root mean square for the
          >>> # guessed slope, rather than the  slope.
          >>> np.isclose(rmse_guessed, 12)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(rmse_guessed, np.sqrt(3148.54 / len(hgb)))
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
