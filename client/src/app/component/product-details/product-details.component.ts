import { Component, OnInit, Input, Inject } from '@angular/core';
import { Product } from 'src/app/model/product.model';
import { MAT_DIALOG_DATA } from '@angular/material';

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.scss']
})
export class ProductDetailsComponent implements OnInit {
  private product: Product;

  constructor(@Inject(MAT_DIALOG_DATA) public data: any) { }

  ngOnInit() {
    this.product = this.data.product;
    console.log(this.product);
  }
}
