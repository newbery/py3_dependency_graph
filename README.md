
# Table of Contents

1.  [What is this tool for?](#org560c33d)
2.  [Usage](#org4fa6ae3)
    1.  [Requirement](#org52604c3)
    2.  [Install the tool](#orgbf52507)
    3.  [use case](#org23288c1)



<a id="org560c33d"></a>

# What is this tool for?

  This is just a simple python static dependency generate tool, It can help you generate the dependency graph
find circular import.


<a id="org4fa6ae3"></a>

# Usage


<a id="org52604c3"></a>

## Requirement

You will need the git and graphviz for the tool

    apt-get update
    apt-get install git graphviz graphviz-dev


<a id="orgbf52507"></a>

## Install the tool

    pip install SDGraph


<a id="org23288c1"></a>

## use case

    SDGraph -f a.py -o dot -n output_name

