import os
from src.perturbator.support_modules.perturbator import branch_insert_process,\
    count_tasks_in,\
    count_sequence_flows_in,\
    count_parallel_gateways_in


def test_parallel_insert_fragment():
    absolute_input_path = os.path.abspath('./tests/test_files/input1.bpmn')
    absolute_input2_path = os.path.abspath('./tests/test_files/input2.bpmn')
    absolute_output_path = os.path.abspath('./tests/test_files/output.bpmn')

    initial_tasks = count_tasks_in(absolute_input_path)
    initial_fragment_tasks = count_tasks_in(absolute_input2_path)
    initial_sequence_flows = count_sequence_flows_in(absolute_input_path)
    initial_fragment_sequence_flows = count_sequence_flows_in(absolute_input2_path)
    initial_gateways = count_parallel_gateways_in(absolute_input_path)
    initial_fragment_gateways = count_parallel_gateways_in(absolute_input_path)

    branch_insert_process(absolute_input_path, absolute_input2_path, 'flow11', 'flow13', absolute_output_path)

    final_sequence_flows = count_sequence_flows_in(absolute_output_path)
    final_gateways = count_parallel_gateways_in(absolute_output_path)
    final_tasks = count_tasks_in(absolute_output_path)

    assert initial_tasks + initial_fragment_tasks == final_tasks
    assert initial_gateways + initial_fragment_gateways + 2 == final_gateways
    assert initial_sequence_flows + initial_fragment_sequence_flows + 2 == final_sequence_flows

