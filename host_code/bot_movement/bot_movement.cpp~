#include <iostream>

using namespace std;

class Point {
public:
	int i, j;
	bool up, down, left, right;
	Point(int ii, int jj) {
		i = ii;
		j = jj;
		up = true;
		down = true;
		left = true;
		right = true;
	}
	/*void set_edges(bool u, bool d, bool l, bool r) {
		up = u;
		down = d;
		left = l;
		right = r;
	}*/
	void set_up(bool u){
		up = u;
	}
	void set_down(bool d){
		down = d;
	}
	void set_left(bool l){
		left = l;
	}
	void set_right(bool r){
		right = r;
	}
};

class Grid {
	int row_count, column_count;
	Point ** points;

public:
	Grid(int r, int c) {
		row_count = r;
		column_count = c;
		points = new (Point*)[row_count];
		for (int i = 0; i < row_count; i++) {
			points[i] = new (Point*)[column_count];
			for (int j = 0; j < column_count; j++) {
				points[i][j] = Point(i, j);
			}
		}

		for(int j = 0 ; j < column_count;j++){
			points[0][j].set_up(false);
			point[row_count - 1][j].set_down(false);
		}
		for(int i = 0 ; i < row_count;i++){
			points[i][0].set_left(false);
			point[i][jcolumn_count - 1].set_right(false);
		}
	}
};

class Bot {
public:
	
};
