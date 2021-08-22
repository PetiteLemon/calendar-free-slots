from slotfinder import SlotFinder


def test_sanity():
    test_input = [
        {
            "name": "Betty",
            "meetings": [
                {
                    "startTime": "2021-03-10T08:55:39+00:00",
                    "endTime": "2021-03-10T09:15:39+00:00",
                    "subject": "Meeting 1"
                },
                {
                    "startTime": "2021-03-10T09:55:39+00:00",
                    "endTime": "2021-03-10T10:15:39+00:00",
                    "subject": "Meeting 2"
                },
                {
                    "startTime": "2021-03-10T11:55:39+00:00",
                    "endTime": "2021-03-10T12:15:39+00:00",
                    "subject": "Meeting 3"
                }]},
        {
            "name": "John",
            "meetings": [
                {
                    "startTime": "2021-03-10T08:15:39+00:00",
                    "endTime": "2021-03-10T09:55:39+00:00",
                    "subject": "Meeting a"
                },
                {
                    "startTime": "2021-03-10T10:15:39+00:00",
                    "endTime": "2021-03-10T10:55:39+00:00",
                    "subject": "Meeting b"
                },
                {
                    "startTime": "2021-03-10T11:15:39+00:00",
                    "endTime": "2021-03-10T12:55:39+00:00",
                    "subject": "Meeting c"
                }]}
    ]
    test_output = [
        {
            'startTime': "2021-03-10T00:00:00+00:00",
            "endTime": "2021-03-10T08:15:39+00:00"
        },
        {
        "startTime": "2021-03-10T10:55:39+00:00",
        "endTime": "2021-03-10T11:15:39+00:00"
        },
        {
        "startTime": "2021-03-10T12:55:39+00:00",
        "endTime": "2021-03-10T23:59:59+00:00"
        }
    ]

    return SlotFinder(test_input).result() == test_output


def test_multiple_days():
    test_input = [
        {
            "name": "Betty",
            "meetings": [
                {
                    "startTime": "2021-03-10T08:55:39+00:00",
                    "endTime": "2021-03-10T09:15:39+00:00",
                    "subject": "Meeting 1"
                },
                {
                    "startTime": "2021-03-10T09:55:39+00:00",
                    "endTime": "2021-03-10T10:15:39+00:00",
                    "subject": "Meeting 2"
                },
                {
                    "startTime": "2021-04-10T08:55:39+00:00",
                    "endTime": "2021-04-10T09:15:39+00:00",
                    "subject": "Meeting 11"
                }]},
        {
            "name": "John",
            "meetings": [
                {
                    "startTime": "2021-03-10T08:15:39+00:00",
                    "endTime": "2021-03-10T09:55:39+00:00",
                    "subject": "Meeting a"
                },
                {
                    "startTime": "2021-03-10T10:15:39+00:00",
                    "endTime": "2021-03-10T10:55:39+00:00",
                    "subject": "Meeting b"
                }]}
    ]
    test_output = [
        {
            'startTime': "2021-03-10T00:00:00+00:00",
            "endTime": "2021-03-10T08:15:39+00:00"
        },
        {
            "startTime": "2021-03-10T10:55:39+00:00",
            "endTime": "2021-04-10T08:55:39+00:00"
        },
        {
            "startTime": "2021-04-10T09:15:39+00:00",
            "endTime": "2021-04-10T23:59:59+00:00"
        }
    ]

    return SlotFinder(test_input).result() == test_output


if __name__ == '__main__':
    print(f"sanity test:{test_sanity()}")
    print(f"multiple days test:{test_multiple_days()}")
