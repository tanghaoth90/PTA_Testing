PROJ_DIR="../projects"
BENCH_INFO="../resources/benchmark_info_full.txt"
STD_DIR="../resources/standardAnswer"
TEST_DIR="../resources/finaltest"

run_score_script:
	python3 score_script.py $(BENCH_INFO) $(STD_DIR) $(TEST_DIR)

run_batch:
	echo "#### Run all student projects."
	python3 batch.py $(PROJ_DIR) $(BENCH_INFO) $(STD_DIR) $(TEST_DIR)

run_check_identical:
	echo "#### Check if the jar file is the example jar. Here is the list:"
	python3 check_indentical.py $(PROJ_DIR)

run_statistics:
	python3 statistics.py

run_full_test: run_batch run_statistics

clean:
	rm -rf score.csv analyzer.jar sootOutput/ __pycache__
