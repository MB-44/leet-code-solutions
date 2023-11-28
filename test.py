def histogram(outcomes, total_outcomes):
    win = GraphWin("Histogram", 600, 600)

    # Draw title and total outcomes text
    title = Text(Point(130, 25), "Histogram Result")
    title.setSize(18)
    title.setStyle("bold")
    title.draw(win)

    total_text = Text(Point(150, 580), f"{total_outcomes} outcomes in total.")
    total_text.setSize(18)
    total_text.setStyle("bold")
    total_text.draw(win)

    # Draw horizontal line for the base of the bars
    line = Line(Point(20, 500), Point(580, 500))
    line.draw(win)

    # Calculate bar heights and positions
    bar_width = 120
    bar_positions = [
        bar_width * 1 + 100 * i
        for i, outcome in enumerate(outcomes.keys())
    ]

    # Draw bars for each outcome
    for i, (outcome, count) in enumerate(outcomes.items()):
        bar_height = 400 * count / total_outcomes
        bar_color = "lightgreen" if outcome == "Progress" else "mediumaquamarine" if outcome == "Trailer" else "green" if outcome == "Retriever" else "yellow"

        bar = Rectangle(Point((bar_positions[i] - bar_width / 2) + 30, 500 - bar_height),Point(bar_positions[i] + bar_width / 2, 500))
        bar.setFill(bar_color)
        bar.draw(win)

        # Draw outcome label above the bar
        xlabel = Text(Point(bar_positions[i], 520),f"{outcome.capitalize()}")
        xlabel.setSize(14)
        xlabel.setStyle("bold")
        xlabel.draw(win)

        ylabel = Text(Point(bar_positions[i], bar_height),f"{count}")
        ylabel.setSize(14)
        ylabel.setStyle("bold")
        ylabel.draw(win)

    # Wait for user to close the window
    win.getMouse()
    win.close()

histogram(outcomes, total_outcomes)