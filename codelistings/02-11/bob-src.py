import linda
linda.connect()

blog = linda.TupleSpace()
linda.universe._out(("MicroBlog",blog))

blog = linda.universe._rd(("MicroBlog",linda.TupleSpace))[1]

blog._out(("bob","distsys","I am studying chap 2"))
blog._out(("bob","distsys","The linda example's pretty simple"))
blog._out(("bob","gtcn","Cool book!"))

