
import React from 'react';
import { View, Text, StyleSheet, FlatList } from 'react-native';
import sampleMeals from '../data/sampleMeals.json';
import MealCard from '../components/MealCard';

export default function MealPlanScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Today's Meal Plan</Text>
      <FlatList
        data={sampleMeals.meals}
        keyExtractor={(item) => item.id}
        renderItem={({item}) => <MealCard meal={item} showDetails />}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container:{flex:1,padding:16},
  title:{fontSize:20,fontWeight:'bold',marginBottom:8}
});
