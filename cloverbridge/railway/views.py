from django.shortcuts import render

# Create your views here.

def get_seat_position(seat_number):
    """
    Method to calculate seat position 
    Already sanitation happend in HTML MIN=0 MAX=72
    Only 8 position available so % 8 will provide the answer
    """
    seat_map = {
        0:"Side Upper", 1:"Left Lower", 2: "Left Middle", 3: "Left Upper",
        4:"Right Lower", 5: "Right Middle", 6: "Right Upper", 7: "Side Lower"
        }
    return seat_map.get(seat_number%8)

def seat_finder(request):
    context = None

    if request.method == "POST":
        seat_number = request.POST.get("seat_number")

        if seat_number:
            position = get_seat_position(int(seat_number))
            context =  {"position_details": {'position':position, 'seat_number': seat_number }}
    return render(request, 'seat_finder.html', context)