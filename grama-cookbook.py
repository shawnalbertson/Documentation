
###
# Create a Grama model
###

# Define the function
def fun_example(X):
    # Name its variables
    x, y, z = X
    return (x + y) ** z
# These must match the order used above!
var_example = ["x", "y", "z"]
# Name the output(s) of the function
out_example = ["f"]

# Grama syntax is a little strange, but is designed to promote readability of code
# using *functional programming patterns* and pipes `>>`
md_example = (
    gr.Model("Example")
    >> gr.cp_function(
        fun=fun_example, # Specify the function
        var=var_example, # Name the input(s)
        out=out_example, # name the output(s)
    )
    >> gr.cp_bounds(
        x=(-1, +1),
        y=(-1, +1),
        z=(0.5, 2.0),
    )
)

# Once built, we can print a helpful summary of a Grama model
md_example.printpretty()

###
# Evaluate Grama model
###
df_res = md_fit >> gr.ev_nominal(df_data)

### 
# Non-Linear Least Squares (NLS)
###
md_fit = gr.fit_nls(
    df_data,
    md=md_example,
    uq_method="linpool",
    seed=101,
    n_restart=1,
)


###
# Vectorized function
###
md_vec = (
    gr.Model()
    # vec_function signals that we're going to provide 
    # a vectorized function
    >> gr.cp_vec_function(
        # Our function needs to both take and return a DataFrame;
        # gr.df_make() is a helper to compactly create a DataFrame
        fun=lambda df: gr.df_make(
            # We can access the variables of the DataFrame provided
            # as an input
            f=df.x + df.y
        ),
        # We still need to specify the inputs, because Grama can't
        # read this information from the lambda function provided
        var=["x", "y"],
        # Ditto for the outputs
        out=["f"],
    )
)

###
# Sinew plots
###
md_example
>> gr.ev_sinews(df_det="swp", n_sweeps=5, n_density=20, seed=101)
>> gr.pt_auto()
