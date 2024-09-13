main_dir = $(shell pwd)
output_dir = Out/79201f37a5f44e30a90f02a902400fccb3f3f1d4

builddocs:
	sphinx-build -M html docs/source/ docs/build/
	mkdir -p $(output_dir)
	cp -R $(main_dir)/docs/build/html/ $(main_dir)/$(output_dir)
	cp -R $(main_dir)/eolian.png $(main_dir)/Out
	cp -R $(main_dir)/index.html $(main_dir)/Out
	




	