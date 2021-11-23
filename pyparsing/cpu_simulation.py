from pyparsing import Word, alphas, nums, Literal, Optional, Keyword


# let's design the grammar of a simple CPU
# loosley inspired by the stuff in CPU_Simulation

grmr = Literal("SA") + Word(nums) ^ Literal("IA") ^ Literal("DA") ^ Literal("SD") + Word(nums)

test_str = """SA 12
              IA
              DA
              SD 100"""

grmr.runTests(test_str)
