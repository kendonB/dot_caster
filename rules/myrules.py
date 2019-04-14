from dragonfly import Repeat, Key


from castervoice.lib import control
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R
from castervoice.lib.dfplus.additions import IntegerRefST

class Decker(MergeRule):
    pronunciation = "test rule"

    mapping = {
        "doon [<nnavi200>]":
            R(Key("pagedown"))*Repeat(extra="nnavi200"),
    }
    extras = [
        IntegerRefST("n", 1, 50),
        IntegerRefST("nnavi200", 1, 200)
    ]

def get_rule():
    return Decker()