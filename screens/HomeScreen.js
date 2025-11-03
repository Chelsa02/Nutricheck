
import React from 'react';
import { View, Text, Button, StyleSheet, FlatList } from 'react-native';
import sampleMeals from '../data/sampleMeals.json';
import MealCard from '../components/MealCard';

export default function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to NutriCheck</Text>
      <Text style={styles.subtitle}>Personalized meal planning for special diets</Text>
      <Button title="View Meal Plan" onPress={() => navigation.navigate('MealPlan')} />
      <Button title="Recommendations" onPress={() => navigation.navigate('Recommendations')} />
      <FlatList
        data={sampleMeals.meals}
        keyExtractor={(item) => item.id}
        renderItem={({item}) => <MealCard meal={item} />}
        style={{marginTop:20}}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container:{flex:1,padding:16},
  title:{fontSize:22,fontWeight:'bold'},
  subtitle:{fontSize:14,marginBottom:12,color:'#444'}
});
