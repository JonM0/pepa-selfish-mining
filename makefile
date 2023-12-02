DOT_FILES := $(wildcard graphs/*.dot)
DOT_GRAPH_TARGETS := $(patsubst graphs/%.dot,out/%.png,$(DOT_FILES))


all: $(DOT_GRAPH_TARGETS)

# Rule to compile each dot file
out/%.png: graphs/%.dot | out
	dot -Tpng $< -o $@

# Create the output directory
out:
	mkdir -p out

# Clean all generated files
clean:
	rm -f $(DOT_GRAPH_TARGETS)

.PHONY: all dot_graphs clean