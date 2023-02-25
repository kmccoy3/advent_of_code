#!/usr/bin/julia

cd("/Users/kmm12/Documents/documents-maul-vader/personal/coding/advent_of_code/2020/day_1")


using DelimitedFiles
using Combinatorics

function my_func(filename)

    data = readdlm("input.csv", ',', Int)

    for p in combinations(data, 2)
        if sum(p) == 2020
            return prod(p)
        end
    end

end

@time my_func("input.csv")
print(@time my_func("input.csv"))