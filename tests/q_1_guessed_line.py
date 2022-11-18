test = {
  'name': 'Question 1_guessed_line',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'ss_guessed'
          >>> 'ss_guessed' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'ss_guesssed'
          >>> # from its initial state (of ...)
          >>> ss_guessed is not ...
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
          >>> hasattr(ss_guessed, 'fun')
          False
          >>> # Here an array with more than one element.
          >>> hasattr(ss_guessed, 'size') and ss_guessed.size > 1
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The answer should be a number for the sum of squares for the
          >>> # guessed slope, rather than the best slope.
          >>> np.isclose(ss_guessed, 707.715)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(ss_guessed, 3148.54)
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
