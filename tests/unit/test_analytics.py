# this tests the analytics functions
import sys

sys.path.append('../use-athena')
import pytest
from helper.analytics import score_ideas


@pytest.mark.parametrize("ideas", [["love is great", "love is boring", "love is crazy"],
                                   ["people are nice", "people are awesome", "people are stupid"]])
def test_db_user_query(ideas):

    ranked_ideas = score_ideas(ideas)

    assert ranked_ideas[0][1] > ranked_ideas[1][1]
    assert ranked_ideas[0][1] > ranked_ideas[2][1]
    assert ranked_ideas[0][1] <= 100
    assert ranked_ideas[2][1] >= 0
