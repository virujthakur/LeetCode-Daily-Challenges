class FoodRatings {
public:
    unordered_map<string,string> foodToCuisine;
    unordered_map<string,int> foodToRating;
    unordered_map<string, set<pair<int,string>>> cuisineToFood;
    
    
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        
        int n=foods.size();
        
        for(int i=0;i<n;i++)
        {
            foodToCuisine[foods[i]]= cuisines[i];
            foodToRating[foods[i]]=-ratings[i];
            cuisineToFood[cuisines[i]].insert({-ratings[i],foods[i]});
        }
        
    }
    
    void changeRating(string food, int newRating) {
        
        int oldRating= foodToRating[food];
        
        foodToRating[food]= -newRating;
        
        string c= foodToCuisine[food];
        
        cuisineToFood[c].erase(cuisineToFood[c].find({oldRating,food}));
        
        cuisineToFood[c].insert({-newRating, food});  
    }
    
    string highestRated(string cuisine) {
        
        set<pair<int,string>> &s= cuisineToFood[cuisine];
        string result;
        
        int rating= s.begin()->first;
        
        for(auto x: s)
        {
            if(x.first!=rating)
                break;
            
            if(result.empty() || x.second<result)
                result=x.second;     
        }
        return result;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */
