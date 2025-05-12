import heapq

class Solution:
    def mostBooked(self, n, meetings):
        # Min-heaps
        available_rooms = list(range(n))  # room numbers
        heapq.heapify(available_rooms)

        ongoing_meetings = []  # (end_time, room_number)
        room_usage = [0] * n

        meetings.sort()

        for start, end in meetings:
            # Free up rooms that have finished meetings
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                _, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, room)

            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
            else:
                # Delay the meeting until the earliest room is available
                earliest_end, room = heapq.heappop(ongoing_meetings)
                duration = end - start
                heapq.heappush(ongoing_meetings, (earliest_end + duration, room))
                # No need to push to available_rooms as it's immediately reused

            room_usage[room] += 1

        # Find the room with the most meetings (smallest number in tie)
        return max(range(n), key=lambda i: (room_usage[i], -i))
