import os
from src.perturbator.support_modules.perturbator import add_new_element_to_flow,\
    count_tasks_in,\
    skip_element,\
    count_sequence_flows_in,\
    count_exclusive_gateways_in


def test_insert_delete_element():
    absolute_input_path = os.path.abspath('./tests/test_files/input1.bpmn')
    absolute_output_path = os.path.abspath('./tests/test_files/output.bpmn')

    initial_tasks = count_tasks_in(absolute_input_path)
    initial_sequence_flows = count_sequence_flows_in(absolute_input_path)
    initial_gateways = count_exclusive_gateways_in(absolute_input_path)

    add_new_element_to_flow(absolute_input_path, 'task', 'flow11', absolute_output_path)
    skip_element(absolute_output_path, 'task12', absolute_output_path)

    final_sequence_flows = count_sequence_flows_in(absolute_output_path)
    final_gateways = count_exclusive_gateways_in(absolute_output_path)
    final_tasks = count_tasks_in(absolute_output_path)

    assert initial_tasks + 1 == final_tasks
    assert initial_gateways + 2 == final_gateways
    assert initial_sequence_flows + 4 == final_sequence_flows

