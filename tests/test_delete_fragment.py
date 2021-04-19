import os
from src.perturbator.support_modules.perturbator import skip_process_fragment,\
    count_tasks_in,\
    count_sequence_flows_in,\
    count_exclusive_gateways_in


def test_delete_fragment():
    absolute_input_path = os.path.abspath('./tests/test_files/input1.bpmn')
    absolute_output_path = os.path.abspath('./tests/test_files/output.bpmn')

    initial_tasks = count_tasks_in(absolute_input_path)
    initial_sequence_flows = count_sequence_flows_in(absolute_input_path)
    initial_gateways = count_exclusive_gateways_in(absolute_input_path)

    skip_process_fragment(absolute_input_path, absolute_output_path, 'flow11', 'flow13')

    final_sequence_flows = count_sequence_flows_in(absolute_output_path)
    final_gateways = count_exclusive_gateways_in(absolute_output_path)
    final_tasks = count_tasks_in(absolute_output_path)

    assert initial_tasks == final_tasks
    assert initial_gateways + 2 == final_gateways
    assert initial_sequence_flows + 3 == final_sequence_flows

