from ariadne import gql, QueryType, make_executable_schema

from .models import Tasks

type_defs = gql(
    """

type Query{
    Hello: String!
    all_tasks(index: Int,  count: Int): [Task]
}
type Task{
    uuid: ID!
    name: String!
    start_date: String!
    end_date: String!
    parent: String!
}

"""
)

query = QueryType()


@query.field("Hello")
def resolve_schools(*_):
    return "Hello world!"


@query.field("all_tasks")
def resolve_all_tasks(*_, count=10, index=0):
    tasks = Tasks.objects.all().order_by("name")
    return tasks[index : index + count]


schema = make_executable_schema(type_defs, query)
