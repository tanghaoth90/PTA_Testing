PROJ_DIR="../projects"
BENCH_INFO="../resources/benchmark_info_simple.txt"
STD_DIR="../resources/standardAnswer"
TEST_DIR="../resources/finaltest"

run_score_script:
	python3 score_script.py $(BENCH_INFO) $(STD_DIR) $(TEST_DIR)

run_batch:
	python3 batch.py $(PROJ_DIR) $(BENCH_INFO) $(STD_DIR) $(TEST_DIR)

run_check_identical:
	python3 check_indentical.py $(PROJ_DIR)

clean:
	rm -rf score.csv analyzer.jar sootOutput/ __pycache__