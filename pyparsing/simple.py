from pyparsing import Word, alphas, nums, Optional

# define grammar of a greeting
greet = Word(alphas) + "," + Word(alphas) + "!"

greet_str = "Hello, World!"
print(greet_str, "->", greet.parseString(greet_str))

# parsing assignemt of integers
assgnmt = Word(alphas) + "=" + Word(nums)
# assignment of floats is more tricky. below works, but produes 3 groups :-(
# assgnmt = Word(alphas) + "=" + Word(nums) + Optional("." + Word(nums))


assgnmt_str = "a = 34"
res = assgnmt.parseString(assgnmt_str)
print(assgnmt_str, "->", res)
# in order to use the int, we need to parse it manually...
print(2*int(res[2]))

nam = Word(alphas)
integer = Word(nums)

assgnmt_v2 = nam("varname") + "=" + integer("value")
res = assgnmt_v2.parseString(assgnmt_str)
print(assgnmt_str, "->", res, repr(res))
print(res["varname"], res["value"])


from pyparsing import pyparsing_common as cm

# there is a predefined f(loating?)number available...
assgnmt_v3 = Word(alphas) + "=" + cm.fnumber()

assgnmt_str2 = "a = 34.67"
res = assgnmt_v3.parseString(assgnmt_str)
print(res, 2*res[2])
res = assgnmt_v3.parseString(assgnmt_str2)
print(res, 2*res[2])
