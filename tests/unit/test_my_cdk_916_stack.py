import aws_cdk as core
import aws_cdk.assertions as assertions

from my_cdk_916.my_cdk_916_stack import MyCdk916Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_cdk_916/my_cdk_916_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MyCdk916Stack(app, "my-cdk-916")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
