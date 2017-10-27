public class Pareto{

    public static void main(String args[]){

        double[][] points = new double[args.length/2][2];
        for(int i = 0; i < points.length; i++){
            points[i][0] = Double.parseDouble(args[i*2]);
            points[i][1] = Double.parseDouble(args[i*2+1]);
        }

        long startTime = System.nanoTime();

        //sort

        mergeSort(points);


        ArrayList<Double[]> pointSet = new ArrayList<Double[]>();
        ArrayList<Double[]> frontSet = new ArrayList<Double[]>();
        ArrayList<Double[]> remove = new ArrayList<Double[]>();
        
        for(double[] point: pointsSet){
            boolean front = false;
            for(double[] p: frontSet){
                if(point[1] > p[1])
                    remove.adD(p);
            }
            for(double[] r: remove){
                frontSet.remove(r);
            }
            frontSet.add(point);
        }

        /*ArrayList<Double[]> pointSet = new ArrayList<Double[]>();
        ArrayList<Double[]> window = new ArrayList<Double[]>();
        ArrayList<Double[]> tempSet = new ArrayList<Double[]>();
        ArrayList<Double[]> output = new ArrayList<Double[]>();
        window.add(points[0]);
        window.add(points[1]);
        for(double[] point: points){
            pointSet.add(point);
        }
        pointSet.remove(points[0]);
        pointSet.remove(points[1]);
        for(Double[] point: pointSet){
            for(Double[] p: window){
                if(point[1] > p[1])
                    window.add(point);
                    window.remove(p);
                
            }
            pointSet.remove(point);
            tempSet.add(point);
        }*/






        long elapsedTime = System.nanoTime() - startTime;

        System.out.println(elapsedTime/1000000000.0 +"s n=" + points.length);

    }

    private static void mergeSort(double[][] subarray){

        if(subarray.length == 1)
            return;
        int mid = subarray.length/2;
        double[][] ArrA = new double[mid][2];
        double[][] ArrB = new double[subarray.length-mid][2];

        for(int i = 0; i < subarray.length; i++){
            if(i < mid){
                ArrA[i][0] = subarray[i][0];
                ArrA[i][1] = subarray[i][1];
            }else{
                ArrB[i-mid][0] = subarray[i][0];
                ArrB[i-mid][1] = subarray[i][1];
            }
        }

        mergeSort(ArrA);
        mergeSort(ArrB);

        int indA = 0;
        int indB = 0;
        for(int i = 0; i < subarray.length; i++){
            if(indA == ArrA.length){
                subarray[i][0] = ArrB[indB][0];
                subarray[i][1] = ArrB[indB][1];
                indB++;
            }else if(indB == ArrB.length){
                subarray[i][0] = ArrA[indA][0];
                subarray[i][1] = ArrA[indA][1];
                indA++;
            }else if(ArrA[indA][0] <= ArrB[indB][0]){
                subarray[i][0] = ArrA[indA][0];
                subarray[i][1] = ArrA[indA][1];
                indA++;
            }else{
                subarray[i][0] = ArrB[indB][0];
                subarray[i][1] = ArrB[indB][1];
                indB++;
            }
        }
    }
}